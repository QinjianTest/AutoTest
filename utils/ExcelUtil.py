import os
import xlrd

#目的：参数化，pytest list
#自定义异常
class SheetTypeError:
    pass
#1、验证文件是否存在，存在读取，不存在报错
class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data=list()
        else:
            raise  FileNotFoundError("文件不存在")
#2、读取sheet方式，名称，索引
    def data(self):
        #存在不读取，不存在读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str,int]:
                raise SheetTypeError("请输入Int or Str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
    #3、读取sheet内容
            #返回list，元素:字典
            #格式[{"a":"a1","b":"b1"},{"a":"a2","b":"b2"}]
            #1.获取首行的信息
            title = sheet.row_values(0)
            #2.遍历测试行，与首行组成dict，放在list
                #1 循环，过滤首行，从1开始
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                #2 与首组成字典，放list
                self._data.append(dict(zip(title, col_value)))

#4、结果返回
        return self._data

# head = ["a","b"]
# value1 = ["a1","b1"]
# value2 =  ["a2","b2"]
# data_list= list()
# #zip
# data_list.append(dict(zip(head,value1)))
# data_list.append(dict(zip(head,value2)))
# #print(dict(zip(head,value1)))
# #print(dict(zip(head,value2)))
# print(data_list)

if __name__ == "__main__":
    reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
    print(reader.data())