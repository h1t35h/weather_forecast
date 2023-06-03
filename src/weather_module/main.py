import argparse
from open_weather import get_weather

def main():
    parser = argparse.ArgumentParser(
        prog="Weather Forecaster",
        description="Simple CLI for getting weather forecast details."
    )

    parser.add_argument('-c','--city')
    args = parser.parse_args()
    print(get_weather(args.city))


if __name__== '__main__':
    main()
