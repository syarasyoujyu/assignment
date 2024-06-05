# assignment
## 使い方:<br>
コマンド上で./run.shとすれば動く<br>
(事前に、.env（ルートディレクトリ上）にGITHUB_TOKENやOPENAI_API_KEYSなどの環境変数を入れる)<br>
.envに入れる環境変数<br>
GITHUB_TOKEN=~~~~ (privateリポジトリにアクセスするためのGITHUB TOKEN)<br>
DATA_PATH=https://github.com/syarasyoujyu/karuta/issues/1# (githubのissues)<br>
CONFIG_FILE=config/default_from_url.yaml<br>
SKIP_EXISTING=False<br>
OPENAI_API_KEY=~~~~~~~~<br>

## 解説：<br>
./run.shと打つことでrun.shが起動する<br>
それによって.envの環境変数を読み取り、その後docker-composeが起動する。<br>
docker-compose.ymlによってsweagent/swe-agent-run:latestを起動し、このファイル上に書いてあったcommandを実行する。<br>
commandの参照URLは'https://princeton-nlp.github.io/SWE-agent/installation/docker/'<br>
docker-compose.ymlのコマンドはSWE-agent上のrun.pyを作動させるもので、その際に必要な変数を記述した。<br>
また、SWE-agentが生成したファイルは、docker-compose.ymlのvolumesによってマウントし、trajectoriesフォルダに残せるようにした。<br>
また、.gitignoreで.envを選んだことによって.envにあるAPI_KEYを流出させずに済む<br>

## 感想：<br>
この課題を通してただコードを書くだけでなく、環境構築も大事であることを改めて痛感しました。<br>
今後はエム二様のためにも、貴社が欲しいと思えるような人材になるためにもこういった研鑽を欠かしたくないと思いました。<br>
