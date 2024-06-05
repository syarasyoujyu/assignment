# assignment
コマンド上で./run.shとすれば動く
(事前に、.env（ルートディレクトリ上）にGITHUB_TOKENやOPENAI_API_KEYSなどの環境変数を入れる)
.envに入れる環境変数
GITHUB_TOKEN=~~~~ (privateリポジトリにアクセスするためのGITHUB TOKEN)
DATA_PATH=https://github.com/syarasyoujyu/karuta/issues/1# (githubのissues)
CONFIG_FILE=config/default_from_url.yaml
SKIP_EXISTING=False
OPENAI_API_KEY=~~~~~~~~

解説：
./run.shと打つことでrun.shが起動する。
それによって.envの環境変数を読み取り、その後docker-composeが起動する。
docker-compose.ymlによってsweagent/swe-agent-run:latestを起動し、このファイル上に書いてあったcommandを実行する。
commandは'https://princeton-nlp.github.io/SWE-agent/installation/docker/'を参考にして作った。
docker-compose.ymlのコマンドはSWE-agent上のrun.pyを作動させるもので、その際に必要な変数を記述した。
また、SWE-agentが生成したファイルは、docker-compose.ymlのvolumesによってマウんティングし、trajectoriesフォルダに残せるようにした。
また、.gitignoreで.envを選んだことによって.envにあるAPI_KEYを流出させずに済む

感想：
この課題を通してただコードを書くだけでなく、環境構築も大事であることを改めて痛感しました。
今後はエム二様のためにも、貴社が欲しいと思えるような人材になるためにもこういった研鑽を欠かしたくないと思いました。
