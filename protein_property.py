import sys

def read_AA_tables(fname):
  AA_abbr=dict()
  with open(fname,'r') as f:
    next(f) # skip the first line 
    for aline in f.readlines():
      #print(aline)
      cols=aline.split(',')
      AA_abbr[cols[1]]=cols[0]
  return AA_abbr

def main():
  print(read_AA_tables(sys.argv[1]))

if __name__ == "__main__":
  main()
