# src/phase_docstring_reference_v1.py
# RCIRCUIT Phase Compute Prototype v1.0
# Auto-generate a simple documentation reference of all key modules.

import inspect
import pkgutil
import importlib

TARGET_PACKAGE = "src"

def extract_docstrings(module_name):
    try:
        module = importlib.import_module(module_name)
    except Exception:
        return None

    docs = {"module": module_name, "items": []}

    for name, member in inspect.getmembers(module):
        if inspect.isclass(member) or inspect.isfunction(member):
            docs["items"].append({
                "name": name,
                "type": "class" if inspect.isclass(member) else "function",
                "doc": inspect.getdoc(member)
            })

    return docs


def generate_reference(package=TARGET_PACKAGE):
    reference = []

    for module_finder, name, ispkg in pkgutil.walk_packages([package]):
        full_name = f"{package}.{name}"
        result = extract_docstrings(full_name)
        if result:
            reference.append(result)

    return reference


if __name__ == "__main__":
    # Minimal preview for documentation testing
    ref = generate_reference("src")
    for module in ref:
        print("\n=== Module:", module["module"], "===")
        for item in module["items"]:
            print(f"- {item['type']} {item['name']}: {item['doc']}")
