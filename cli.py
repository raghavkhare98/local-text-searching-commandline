import argparse
from main import run_search

def main():
    parser = argparse.ArgumentParser(description="Local full-search engine")
    parser.add_argument("--path", help="Provide a path for the directory where you want to perform this search")
    parser.add_argument("--query", help="Enter your search term. Multiple words/a sentence can be searched")
    args = parser.parse_args()

    results = run_search(args.path, args.query)

    if not results:
        print("No results found")
    
    else:
        print(f"Matches for '{args.query}': \n")
        for file, positions in results.items():
            print(f"- {file} found at {len(positions)} positions")

if __name__=="__main__":

    main()