
# Unittest Tutorial

Pythonコードをテストするための標準ライブラリであるunittestについてのチュートリアルプロジェクト。

# Usage

unittestは基本的には、

1. unittest.TestCaseを親クラスに持つクラスを定義する。

2. テスト関数名はtestを接頭語に持たせる。

3. テスト結果の判定にはunittest側で用意されているものを使用する。(self.assertEqualなど)

4. 実行はunittest.main()で、記述したテストをすべてunittestが自動的に実行してくれる。

# subTest

unittestのtest関数で判定を行うためのアサーションメソッド(assertEqualなど)は、その判定に一致しない場合、その場でテストを中止しAssertionErrorを発生させてしまう。

そのため、1つのテストの中でfor文などを使用して一気に引数を変更してテストを行う方法は推奨されない。

```

def test_for(self):
	# もし一度エラーが発生してしまうと、その場でテスト自体終了してしまう。
	for i in range(10000):
		result = hoge(i)
	self.assertEqual(result,i*100)

```

そこで便利になるのが、subTest。

失敗にかかわらず、与えたパターンすべてを実行してくれるのでテスト関数ないでfor文を使用して例外処理をするという面倒なことをしなくても処理してくれる。下記が実行例。

```

def test_hoge(self):
	patterns = [
	(1,10),
	(2,20),
	(3,30),
	(10,100),
	]

	for x,res in patterns:
		# これで失敗したときに表示する内容を引数に渡す
		with self.subTest(arg=x,result=res):
			self.assertEqual(hoge(x),res)
```

# Exception

もちろん例外処理についてのテストをすることもできる。つまり、発生しうるエラーやエラーが持つ値などをテストする。

```

def test_except(self):
	#　例外テストの場合は、発生し得る例外をテスト実行前に記述しておく
	with self.assertRaises(TypeError):
		#　実行するテストスクリプト
		exception()


```

これでテストスクリプトが発生させる例外の種類をテストできるようになった。また例外が持つ値についてテストを実行したい場合は、

```

def test_except(self):
	#　例外テストの場合は、発生し得る例外をテスト実行前に記述しておく
	with self.assertRaises(TypeError) as ar:
		#　実行するテストスクリプト
		exception()
	
	# 例外オブジェクトをunittestから取得する	
	exc = ar.exception

	# 取得した例外オブジェクトの中身の値を使ってさらにテストすることができる。
	self.assertEqual(exception.hello,10)

```

# Stdout

unittestを使えば、標準出力に表示される文字に関してのテストを行うこともできる。

```

class StdoutTest(unittest.TestCase):
        def test_stdout(self):
                io = StringIO()
		# 標準出力をStringIOにリダイレクト
                with redirect_stdout(io):
                        hoge("hello world")
		# printのときは最後に\nも出力されるので注意
                self.assertEqual(io.getvalue(),"hello world\n")

```

# mock

テストコードの中で使用している、別のオブジェクトを置き換える機能。つまり、テスト対象のコード内のオブジェクトをテストコードから操作することで様々な環境変化(例えば、socketの接続先を変更したり)を想定したテストを実現する機能。

基本的な操作は、

1. モックを作成する

2. 動作変更するオブジェクトにパッチを当てる


mockに設定したオブジェクトが正しい引数を元に呼び出されたかどうかなどをテストできる。

```

class Mock(unittest.TestCase):
        def test_mock(self):
		# mockの作成
                m = unittest.mock.MagicMock()
		# 対象関数にmockを設定
                os.path.abspath = m

                hoge("hello")
		# 正しい引数で呼び出されたかどうかのテスト
                m.assert_called_with("hello")


```
