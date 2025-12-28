import json

class MatrixEngine:
    def __init__(self, spec_path):
        with open(spec_path, 'r') as f:
            self.spec = f.read()
        print("BNU_MATRIX Engine Initialized.")

    def load_capsule(self, capsule_path):
        with open(capsule_path, 'r') as f:
            capsule = json.load(f)
        print(f"Loading Capsule: {capsule['name']}...")
        return capsule

    def generate_prompt(self, agent_name, capsule):
        # 模拟根据规格说明书合成最终 Prompt
        final_prompt = f"System: {self.spec}\nAgent: {agent_name}\nActive Capsule: {capsule['name']}\nLogic: {capsule['logic_core']}"
        return final_prompt

if __name__ == "__main__":
    engine = MatrixEngine("../spec/prompt_spec_v2.md")
    capsule = engine.load_capsule("../library/academic_neural_link/capsule.json")
    print("\n--- Generated Agent Prompt ---\n")
    print(engine.generate_prompt("Kai", capsule))