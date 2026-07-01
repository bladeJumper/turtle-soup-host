# 汤底别偷看

线下海龟汤主持用静态题库。手机打开即可用。

## 功能

- 随机抽题
- 标签 / 难度 / 搜索筛选
- 玩家可看的汤面
- 主持人折叠汤底和提示
- localStorage 标记已玩
- 当前题库 100 题，均从公开网络题库整理（保留 `source` / `sourceUrl` 字段；已排除“电梯”题）

## 本地运行

```bash
cd /home/zhuojun/turtle-soup-host
python3 -m http.server 4173
```

打开：http://127.0.0.1:4173

## 部署

### GitHub Pages

把本目录推到 GitHub 仓库，Settings → Pages → Deploy from branch → main / root。

### Cloudflare Pages

连接 GitHub 仓库，构建命令留空，输出目录填 `/`。

## 加题

编辑 `puzzles.json`，新增对象即可：

```json
{
  "id": "013",
  "title": "标题",
  "difficulty": 3,
  "tags": ["经典", "本格"],
  "surface": "汤面",
  "answer": "汤底",
  "hostNotes": ["主持提示 1", "主持提示 2"],
  "source": "original/adapted"
}
```
