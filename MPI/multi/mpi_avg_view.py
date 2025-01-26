from mpi4py import MPI
import csv
import time

def process_chunk(rows):
    # process each chunk and return the country views (sum and count)
    country_views = {}
    for row in rows:
        country = row[6]  # column 7  is the country
        views = int(row[7])  # column 8 is the number of views
        if country not in country_views:
            country_views[country] = {'sum': 0, 'count': 0}
        country_views[country]['sum'] += views
        country_views[country]['count'] += 1
    return country_views


def main():
    # MPI setup
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    averages = []


    # root process reads the file and split data as evenly as possible
    if rank == 0:
        time_start = time.time() # start the timer
        print('time started')
        filename = 'input.csv'  # input CSV file (changed based on dataset sizes)
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as infile:
                print(f"File {filename} opened successfully")
                reader = csv.reader(infile)
                next(reader)  # skip the header
                rows = list(reader)  # read all rows into memory
        except Exception as e:
            print(f"Error opening file: {e}")
            comm.Abort()
        num_lines = len(rows)
        
        # calculate base lines per process and extra lines
        base_lines = num_lines // size
        remainder = num_lines % size
        
        chunks = []
        start = 0
        for i in range(size):
            # determine the number of lines for this process
            num_lines_for_process = base_lines + (1 if i < remainder else 0)
            end = start + num_lines_for_process
            chunks.append(rows[start:end])   # append a list of rows
            start = end  # move to the next chunk
        print('Done splitted')

    else:
        chunks = None

    # scatter the chunks of rows to all processes
    chunk = comm.scatter(chunks, root=0)

    # each process processes its chunk and computes local sums and counts
    local_country_views = process_chunk(chunk)

    # gather the results from all processes to root process
    all_country_views = comm.gather(local_country_views, root=0)

    if rank == 0:
        print('start accumulating')
        # root process aggregates the results
        final_country_views = {}

        for country_views in all_country_views:
            for country, data in country_views.items():
                if country not in final_country_views:
                    final_country_views[country] = {'sum': 0, 'count': 0}
                final_country_views[country]['sum'] += data['sum']
                final_country_views[country]['count'] += data['count']

        # compute and print the average views per country
        for country, data in final_country_views.items():
            average = round(data['sum'] / data['count'] if data['count'] != 0 else 0, 2)
            averages.append((country, average))

        # sort averages by value in descending order and get the top 5
        top_5 = sorted(averages, key=lambda x: x[1], reverse=True)[:5]
        
        # print the top 5 countries and their averages
        for country, average in top_5:
            print(f"{country}: {average}")
            
        time_end = time.time() # stop the timer
        
        # calculate and print the elapsed time
        elapsedTime = time_end - time_start
        print(f'The elapsed time is {elapsedTime} seconds')



if __name__ == "__main__":
    main()
