# Multi-Agent Learning Assistant System (Advanced Version)
# 模块化 + 面向对象 + 多Agent协作

from datetime import datetime


class Logger:
    """简单日志模块"""
    @staticmethod
    def log(message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


class BaseAgent:
    """Agent基类"""
    def __init__(self, name):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError


class ParsingAgent(BaseAgent):
    """问题解析 Agent"""
    def run(self, question):
        Logger.log(f"{self.name} 正在解析问题...")
        if "二叉树" in question:
            return "data_structure"
        elif "回归" in question:
            return "machine_learning"
        return "general"


class ReasoningAgent(BaseAgent):
    """推理 Agent（模拟CoT）"""
    def run(self, question):
        Logger.log(f"{self.name} 正在进行推理...")
        return [
            "Step1: 分析题目需求",
            "Step2: 确定算法或模型",
            "Step3: 设计实现逻辑",
            "Step4: 验证结果正确性"
        ]


class CodeAgent(BaseAgent):
    """代码生成 Agent"""
    def run(self, task_type):
        Logger.log(f"{self.name} 正在生成代码...")
        if task_type == "data_structure":
            return """class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)"""
        return "# TODO: generate code"


class VerificationAgent(BaseAgent):
    """结果校验 Agent"""
    def run(self, code):
        Logger.log(f"{self.name} 正在校验结果...")
        if "class" in code and "def" in code:
            return "✔ 代码结构完整"
        return "✘ 代码可能存在问题"


class LearningAssistantSystem:
    """多Agent调度系统（核心）"""

    def __init__(self):
        self.parser = ParsingAgent("ParsingAgent")
        self.reasoner = ReasoningAgent("ReasoningAgent")
        self.coder = CodeAgent("CodeAgent")
        self.verifier = VerificationAgent("VerificationAgent")

    def solve(self, question):
        Logger.log("系统启动")

        # 1. 问题解析
        task_type = self.parser.run(question)
        Logger.log(f"识别任务类型: {task_type}")

        # 2. 推理
        steps = self.reasoner.run(question)
        Logger.log("推理步骤生成完成")

        # 3. 代码生成
        code = self.coder.run(task_type)

        # 4. 校验
        result = self.verifier.run(code)

        # 输出结果
        print("\n=== 最终输出 ===")
        print("问题:", question)
        print("\n推理步骤:")
        for step in steps:
            print("-", step)

        print("\n生成代码:\n", code)
        print("\n校验结果:", result)

        Logger.log("任务完成")


# 测试运行
if __name__ == "__main__":
    system = LearningAssistantSystem()
    system.solve("请实现二叉树的前序遍历")
