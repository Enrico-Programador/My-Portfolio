from block_markdown import block_to_block_type, markdown_to_blocks


def main():
    print("running main...")
    md = """
1. This is a
2. quote block
3. very quoty
"""
    blocks = block_to_block_type(md)
    print(f"Return value: {blocks}")
main()