# CREATE TABLE public.inputs_09 PARTITION OF public.inputs_src FOR VALUES FROM('2009-01-01 00:00:00') TO('2010-02-01 00:00:00')


year = 9
month = 1
day = 1
while year <= 24:
    if year < 10:
        if month < 10:
                f = open("./BTC/tt.sql", "a+")
                f.write(
                    f"CREATE TABLE public.out_{year}_{month}_{day} PARTITION OF public.output FOR VALUES FROM('200{year}-0{month}-{day} 00:00:00') TO('200{year}-0{month}-{day} 23:59:59');\n")
        else:
            f = open("./BTC/tt.sql", "a+")
            f.write(
                    f"CREATE TABLE public.out_{year}_{month}_{day} PARTITION OF public.output FOR VALUES FROM('200{year}-{month}-{day} 00:00:00') TO('200{year}-{month}-{day} 23:59:59');\n")
    else:
        if month < 10:
                f = open("./BTC/tt.sql", "a+")
                f.write(
                    f"CREATE TABLE public.out_{year}_{month}_{day} PARTITION OF public.output FOR VALUES FROM('20{year}-0{month}-{day} 00:00:00') TO('20{year}-0{month}-{day} 23:59:59');\n")
        else:
            f = open("./BTC/tt.sql", "a+")
            f.write(
                    f"CREATE TABLE public.out_{year}_{month}_{day} PARTITION OF public.output FOR VALUES FROM('20{year}-{month}-{day} 00:00:00') TO('20{year}-{month}-{day} 23:59:59');\n")
        
    if day == 31:
        month += 1
        day = 0
    if month == 13:
        year += 1
        month = 1
    day += 1
