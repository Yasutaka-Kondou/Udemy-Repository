import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit入門")

st.write("Display Image")

"Start"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Ineration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Dane!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ボタンがおされました")

expander = st.expander("問い合わせ")
expander.write("回答")

expander2 = st.expander("問い合わせ2")
expander2.write("回答2")

# text = st.text_input("あなたの趣味を教えてください")
# condition = st.slider("あなたの調子は？", 0, 100, 50)

# "あなたの趣味は、", text, "です。"
# "コンディション、", condition, "です。"

# option = st.selectbox(
#     "あなたの好きな数字を教えてください",
#     list(range(1, 11))
# )

# "あなたの好きな数字は、", option, "です。"

# if st.checkbox("Show Image"):
#     img = Image.open("20170718_020442228_iOS.jpg")
#     st.image(img, caption="写真", use_container_width=True)

st.write("DataFlame")

#df = pd.DataFrame({
#    "1列目":[1, 2, 3, 4],
#    "2列目":[10, 20, 30, 40]
#})

#st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)
#st.table(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/(50, 50) + (35.69, 139.70),
    columns=["lat", "lon"]
)
st.map(df)




#
"""
# 章
## 節
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

