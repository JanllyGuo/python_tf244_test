'''
安裝完畢後，我們來編寫一個簡單的程式來驗證安裝
'''
import tensorflow as tf

A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.matmul(A, B)

print(C)