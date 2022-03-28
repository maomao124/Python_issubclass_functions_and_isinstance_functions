"""
 * Project name(项目名称)：Python_issubclass函数和isinstance函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 13:30
 * Version(版本): 1.0
 * Description(描述)：  __bases__ 属性
 """


class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C):
    pass


if __name__ == '__main__':
    print('类A的所有父类:', A.__bases__)
    print('类B的所有父类:', B.__bases__)
    print('类C的所有父类:', C.__bases__)
    print('类D的所有父类:', D.__bases__)

