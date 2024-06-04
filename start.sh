#!/bin/bash

# APIキーの設定ファイルの読み込み
source .env

# Docker Compose を使ってサービスを起動
docker-compose up --build -d
