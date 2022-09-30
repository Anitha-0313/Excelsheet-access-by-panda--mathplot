import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('st.xlsx')
print(df)
plt.plot(df['Grade'])

plt.show()
           
