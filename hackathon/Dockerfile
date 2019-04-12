FROM private-registry.sohucs.com/domeos-pub/python:3.6.2-centos

# 镜像维护人员
MAINTAINER weiwang216168@sohu-inc.com

USER root

# 设置环境变量，使其支持中文
ENV LANG "en_US.UTF-8"

# 设置工程名称
ENV module=mp-content-location-judge

# 创建目录
ENV DIR=/opt/apps/${module}

# 设置工作目录
WORKDIR $DIR

# 安装依赖包
ADD requirements.txt ${DIR}/
RUN export PATH=/usr/local/python3/bin:$PATH && pip3 install -r requirements.txt

# 拷贝项目源码
ADD ./ $DIR

# CMD
WORKDIR $DIR
ENTRYPOINT exec python run.py