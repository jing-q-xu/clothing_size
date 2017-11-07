# clothing_size
clothing size converter

## usage

``` python
import size_converter_error as sc_error
from converter import convert_size
from data_loader import load_config_files

if __name__ == '__main__': 
    try:
        load_config_files()
        print (convert_size("women top", "国际", "意大利", "XXS")) 
        print (convert_size("women top", "国际", "英国", "XXS")) 
        print (convert_size("women top", "国际", "丹麦", "XXS"))
        print (convert_size("men shoes", "中国", "意大利", "38"))
        print (convert_size("men shoes", "英国", "美国", "5"))
    except sc_error.SizeConverterError as e:
        print(e)
```
