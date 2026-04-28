# Multi-Agent Learning Assistant System

## 项目简介
本项目是一个基于大模型（LLM）的多Agent学习辅助系统，旨在提升编程与数据科学学习效率。

## 核心功能
- 自动解析学习问题（数据结构 / 编程 / 机器学习）
- 基于Chain-of-Thought进行推理
- 自动生成代码并附带注释
- 结果校验与优化

## 系统架构
系统采用多Agent协作机制：
- Parsing Agent：问题解析
- Reasoning Agent：推理生成
- Code Agent：代码生成
- Verification Agent：结果校验

## 技术特点
- Multi-Agent Orchestration
- Chain-of-Thought 推理
- 可扩展架构设计

## 使用方式
```bash
python multi_agent_system.py
