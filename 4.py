data = [
    {"mod": "RDX", "yr": 2009},
    {"mod": "LS", "yr": 2000},
    {"mod": "GLK", "yr": 2010},
    {"mod": "Ex1500", "yr": 2005},
    {"mod": "LR2", "yr": 2008},
    {"mod": "XF", "yr": 2012},
    {"mod": "MR2", "yr": 2005},
    {"mod": "Malibu", "yr": 2007},
    {"mod": "MCls", "yr": 2010},
    {"mod": "Rout", "yr": 2011}
]

data.sort(key=lambda x: x["yr"])

for d in data:
    print(f"Model: {d['mod']}, Year: {d['yr']}")

