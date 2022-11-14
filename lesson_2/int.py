int_var = 12332111223486981642391332135
int_var1 = str(int_var)
int_var2 = list(int_var1)
int_var3 = set(int_var2)
int_var4 = sorted(int_var3)
int_var4.sort(reverse=True)

print(int_var4)