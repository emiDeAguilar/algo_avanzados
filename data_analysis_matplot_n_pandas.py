
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_data.csv')

# data.price.replace(('vhigh','high','med','low'), (4,3,2,1), inplace = True)

# data.rating.replace(('vhigh','high','med','low'), (4,3,2,1), inplace = True)

dataset = data.values



# prices = data['price'].value_counts()
# prices.plot(kind='bar')

# #Plots
# colors=['red', 'blue', 'green', 'orange']
# prices.plot(kind='bar', color=colors)
# plt.xlabel('Price Category')
# plt.ylabel('Count')
# plt.title('Distribution of Price Categories')

# rear_camera = data['rear_camera_max_mp'].value_counts()
# rear_camera.plot(kind='bar', color=colors)
# plt.xlabel('Rear Camera Max MP')
# plt.ylabel('Count')
# plt.title('Distribution of Rear Camera Max MP')

memory_card_max_size = data['memory_card_max_gb'].value_counts()

explode = [0.1 if i == memory_card_max_size.max() else 0 for i in memory_card_max_size]
plt.pie(memory_card_max_size, labels=memory_card_max_size.index, shadow=True, autopct='%.2f%%')
plt.title('Distribution of Memory Card Max Size (GB)')
plt.axis('off')
plt.legend(loc = 'best', title='Memory Card Max Size (GB)', bbox_to_anchor=(1.05, 1))


memory_card_type = data['memory_card_type'].value_counts()
memory_card_type.replace(('Dedicated', 'Hybrid'),(0,1), inplace=True)


texts=[
    'shape',
    'columns',
    'dtypes',
    'head',
    'tail',
    'info',
    'sample (10)',
    'sample (10) of rating',
    'memory card type unique',
    'memory card type value counts'
    
]

texts = [text.upper() for text in texts]

printable =[
data.shape,
data.columns,
data.dtypes,
data.head(),
data.tail(),
data.info(),
data.sample(10),
data.rating.head(),
data['memory_card_type'].unique(),
data['memory_card_type'].value_counts(),
# data['price'].head(5),
# prices,
# data['price'].value_counts().sort_index(ascending=False),

]
for i in range(len(printable)):
    print(f'*** {texts[i]} ***')
    print(printable[i])
    print("\n")
    print("--------------------------------------------------")
    
for column in data.columns:
    print(f"Unique values in column '{column}':")
    print(data[column].unique())
    print("\n")
    print(f"Value counts in '{column}':")
    print(data[column].value_counts())
    print("\n")
    print("--------------------------------------------------")



plt.show()