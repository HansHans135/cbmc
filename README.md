# cbmc
麥塊匿名發文平台 api for python

# 安裝
```
pip install cbmc
```

# 使用

```py
from cbmc import onpost
import cbmc

#當有新文章時
async def on_post(updated):
    print(f"有新的資料!!\n{updated}")
onpost(on_update=on_post)

#用編號取得文章(無則返回None)
cbmc.get_post(1)

#取得文章列表(最大300)
cbmc.post_list(1)
```