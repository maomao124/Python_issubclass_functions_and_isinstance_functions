"""
 * Project name(项目名称)：Python_issubclass函数和isinstance函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:29
 * Version(版本): 1.0
 * Description(描述)：
 issubclass(cls, class_or_tuple)：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
isinstance(obj, class_or_tuple)：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。

 """

if __name__ == '__main__':
    # 定义一个字符串
    hello = "Hello"
    # "Hello"是str类的实例，输出True
    print('"Hello"是否是str类的实例: ', isinstance(hello, str))
    # "Hello"是object类的子类的实例，输出True
    print('"Hello"是否是object类的实例: ', isinstance(hello, object))
    # str是object类的子类，输出True
    print('str是否是object类的子类: ', issubclass(str, object))
    # "Hello"不是tuple类及其子类的实例，输出False
    print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
    # str不是tuple类的子类，输出False
    print('str是否是tuple类的子类: ', issubclass(str, tuple))
    # 定义一个列表
    my_list = [2, 4]
    # [2, 4]是list类的实例，输出True
    print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
    # [2, 4]是object类的子类的实例，输出True
    print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
    # list是object类的子类，输出True
    print('list是否是object类的子类: ', issubclass(list, object))
    # [2, 4]不是tuple类及其子类的实例，输出False
    print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
    # list不是tuple类的子类，输出False
    print('list是否是tuple类的子类: ', issubclass(list, tuple))

    data = (20, '123')
    print('data是否为列表或元组: ', isinstance(data, (list, tuple)))  # True
    # str不是list或者tuple的子类，输出False
    print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
    # str是list或tuple或object的子类，输出True
    print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))
