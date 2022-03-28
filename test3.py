"""
 * Project name(项目名称)：Python_issubclass函数和isinstance函数
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:32
 * Version(版本): 1.0
 * Description(描述)： 
 """


class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C):
    pass


class E(A, B):
    pass


if __name__ == '__main__':
    print('类A的所有子类:', A.__subclasses__())
    print('类B的所有子类:', B.__subclasses__())
    print('类C的所有子类:', C.__subclasses__())
    print('类D的所有子类:', D.__subclasses__())
    print('类E的所有子类:', E.__subclasses__())
