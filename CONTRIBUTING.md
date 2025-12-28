# 🧠 Open-Matrix-Standard (OMS) 开发者贡献指南

感谢你关注 **Open-Matrix-Standard (OMS)**！校园不仅仅是教室的集合，它是一个充满动态知识与逻辑涌现的“矩阵”。我们邀请你一起，为每一所中学构建属于它的数字灵魂。

---

## 📢 开发者招募令 (Call for Contributors)

### 为每一所中学构建数字灵魂
我们正在寻找：
- **知识胶囊架构师**：将学科知识（物理、历史、艺术等）转化为 AI 可感知的“知识胶囊”。
- **Prompt 工程师**：优化 OMS 的核心五层交互逻辑。
- **场景布道师**：将 OMS 适配到你的学校，结合地图与教务系统实现落地。

---

## 🚀 快速上手：如何开发一个“知识胶囊”？

在 OMS 中，**知识胶囊 (Capsule)** 是智能体的灵魂。它让 AI 具备了身份、知识边界和场景感知能力。

### 1. 定义你的胶囊 (Identity)
确定你要解决的校园场景：
- **学术型**：如“附中物理实验室助手”。
- **文化型**：如“银杏大道历史叙事者”。
- **生活型**：如“校猫图鉴与投喂指南”。

### 2. 编写 `capsule.json` 配置文件
在 `library/` 下创建你的插件文件夹，并包含一个规范的 JSON 文件。

```json
{
  "id": "capsule-your-id",
  "name": "插件名称",
  "version": "2.0",
  "logic_core": "LiveLinkVision", 
  "capabilities": ["能力关键词1", "能力关键词2"],
  "grounding_source": {
    "google_search": true,
    "google_maps": true
  }
}
