import pandas as pd
import argparse
import pyarrow.parquet as pq


def get_args():
    parser = argparse.ArgumentParser(description="Convert")
    parser.add_argument('--csv2parquet', dest='csv2parquet', nargs=2, type=str,
                        help='converts csv files to parquet')
    parser.add_argument('--parquet2csv', dest='parquet2csv', nargs=2, type=str,
                        help='converts parquet files to csv')
    parser.add_argument('--get-schema', dest='get_schema', nargs=1, type=str,
                        help='shows schematics parquet file')
    return parser.parse_args()


def chek_src_file(name):
    try:
        open(name)
    except Exception as ex:
        print('unable to access file ' + name)


def convert_csv_to_parquet(src_filename, dst_filename):
    try:
        df = pd.read_csv(src_filename)
        df.to_parquet(dst_filename, compression='UNCOMPRESSED', engine='fastparquet')
    except Exception as ex:
        print('failed to write file. Error {}:{}'.format(ex.strerror, ex.filename))


def convert_parquet_to_csv(src_filename, dst_filename):
    try:
        df = pd.read_parquet(src_filename, engine='fastparquet')
        df.to_csv(dst_filename, index=False)
    except Exception as ex:
        print('failed to write file. Error {}:{}'.format(ex.strerror, ex.filename))



def get_schema(filename):
    try:
        with open(filename, 'r') as f:
            table = pq.read_table(filename)
        return table.schema
    except Exception as ex:
        print('failed to get schema Error {}:{}'.format(ex.strerror, ex.filename))


def main():
    pars = get_args()
    print("ARGUMENTS:")
    args = [pars.csv2parquet, pars.parquet2csv, pars.get_schema]

    if args[0] != None:
        convert_csv_to_parquet(args[0][0], args[0][1])
    elif args[1] != None:
        convert_parquet_to_csv(args[1][0], args[1][1])
    elif args[2] != None:
        print(get_schema(args[2][0]))
    else:
        print('To get started, enter one of the parameters:'
              ' --csv2parquet, --parquet2csv, --get-schema or --help')


if __name__ == '__main__':
    main()
