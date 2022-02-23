# twitter_automation
Twitter運用の自動化スクリプト集です。

## comands
### auto_follow
Twitterの自動フォロースクリプトです。
第一引数に気になる単語を指定するだけで、関連するユーザを自動フォローします。

### auto_unfollow
片思い（自分がフォローしているが、相手がフォローしていない状態）を解消します。

# Requirement

* Python 3.X.X
 
# Installation
 
```bash
pip install requirement.txt
mv config.ini.example config.ini
```

※ config.iniの編集が必須です。
詳細に関しては、
[こちら](https://nekonisi.com/autofollow)をご確認ください
 
# Usage
  
```bash
./auto_follow {search_words}
./auto_unfollow
```
 
# Note
※ スパムと間違えられて、アカウントが凍結する可能性があるのでご注意ください。

# Author
  
* nekonisi
* https://nekonisi.com
* konishi2175@gmail.com
 
# License
ライセンスを明示する
 
"tweepy_auto_follow" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
