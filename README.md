# python_tf244_test
本地端的 Python 虛擬環境 ( 含 TensorFlow 2.4.4)


1. 開發環境及工具
   * Win7 64bit
   * Python 3.8.6
   * Visual Studio Code
   
2. 建立虛擬環境
```
  cd 程式資料夾路徑

  virtualenv venv
  pip list

  venv\Scripts\activate
  pip list

  pip install tensorflow-cpu == 2.4.4
  pip list
```

3. Tensorflow 安裝完畢後，編編寫一個簡單的程式來驗證安裝，參考連結

https://tf.wiki/zh_hant/basic/installation.html

**如果發生錯誤: You may install these DLLs by downloading "Microsoft C++ Redistributable for Visual Studio 2015, 2017 and 2019" for ....**

4. 執行程式
```python
  python main.py
```
