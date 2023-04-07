
import argparse

parser = argparse.ArgumentParser(description='Calculate employee salary')
parser.add_argument('hours', type=int, help='Work hours')
parser.add_argument('rate', type=float, help='Hourly rate')
parser.add_argument('bonus', type=float, help='Bonus')

args = parser.parse_args()

salary = args.hours * args.rate + args.bonus
print(f"Employee salary: {salary}")
