import sys

date = sys.argv[1]
text = "urlaub philipp #date#\n\n\nhallo olli,\nhiermit beantrage ich urlaub fuer den zeitraum vom #date#.\n\nviele gruesse,\nphilipp"
sys.stdout.write(text.replace('#date#', date))