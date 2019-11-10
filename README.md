# 機械学習等の練習問題

## この問題集の使い方

まずは、パソコンにこのrepositoryをcloneしましょう。

```bash
git clone https://github.com/Stealthmate/saidai-deep-learning-problems.git
```

次に、Jupyterを起動しましょう。

```bash
cd saidai-deep-learning-problems
jupyter notebook
```

問題毎にディレクトリが分かれています。各問題は一つのNotebookでやりますが、原本を保持するために、編集する前にコピーを作って、コピーを編集しましょう。例えば：

```bash
cd 01-multivariate-linear-regression
cp my-notebook.ipynb
```

## 更新方法

問題を臨時追加していくので、新しい問題を落とす時は以下のコマンドを使いましょう：

```bash
cd saidai-deep-learning-problems
git pull origin master
```
