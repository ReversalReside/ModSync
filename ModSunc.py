import os
import re
from datetime import datetime

def clean_filename(filename):
    """Removes numbering from filename (e.g., '1. ', '10. ', '100. ')"""
    cleaned = re.sub(r'^\d+\.\s*', '', filename)
    cleaned = cleaned.strip()
    return cleaned

def compare_with_reference_list(folder_path, reference_file="reference_list.txt"):
    """
    Compares files in folder with reference list from txt file
    (ignores numbering in the reference list)
    """
    
    # 1. Read reference list from txt file and clean from numbering
    reference_path = os.path.join(folder_path, reference_file)
    
    if not os.path.exists(reference_path):
        print(f"❌ Error: File '{reference_file}' not found!")
        return
    
    reference_files = []
    with open(reference_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('=') and not line.startswith('File list') and not line.startswith('Total'):
                cleaned = clean_filename(line)
                if cleaned:
                    reference_files.append(cleaned)
    
    # 2. Get list of actual files in the folder
    script_name = os.path.basename(__file__)
    all_items = os.listdir(folder_path)
    
    actual_files = []
    for item in all_items:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item not in [script_name, reference_file, "comparison_result.txt"]:
            actual_files.append(item)
    
    # 3. Compare
    reference_set = set(reference_files)
    actual_set = set(actual_files)
    
    missing_files = reference_set - actual_set
    extra_files = actual_set - reference_set
    common_files = reference_set & actual_set
    
    # 4. Display results
    print("\n" + "=" * 70)
    print("FILE COMPARISON RESULTS")
    print("=" * 70)
    print(f"Folder: {folder_path}")
    print(f"Reference list: {reference_file}")
    print("-" * 70)
    
    if missing_files:
        print(f"\n❌ MISSING FILES ({len(missing_files)} pcs):")
        for i, file in enumerate(sorted(missing_files)[:20], 1):
            print(f"   {i}. {file}")
        if len(missing_files) > 20:
            print(f"   ... and {len(missing_files) - 20} more files")
    else:
        print(f"\n✅ All files from the list are present!")
    
    if extra_files:
        print(f"\n⚠️ EXTRA FILES (not in list) ({len(extra_files)} pcs):")
        for i, file in enumerate(sorted(extra_files)[:20], 1):
            print(f"   {i}. {file}")
        if len(extra_files) > 20:
            print(f"   ... and {len(extra_files) - 20} more files")
    
    print(f"\n📊 STATISTICS:")
    print(f"   Total in reference: {len(reference_files)} files")
    print(f"   Present: {len(common_files)} files")
    print(f"   Missing: {len(missing_files)} files")
    print(f"   Extra: {len(extra_files)} files")
    
    if len(common_files) == len(reference_files):
        print("\n🎉 PERFECT! All files from the list are in place!")
    elif len(common_files) > 0:
        print(f"\n📁 Found {len(common_files)} out of {len(reference_files)} required files")
    
    # 5. Save detailed report
    result_file = os.path.join(folder_path, "comparison_result.txt")
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("DETAILED FILE COMPARISON REPORT\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Folder: {folder_path}\n")
        f.write(f"Reference: {reference_file}\n\n")
        
        f.write("-" * 70 + "\n")
        f.write(f"❌ MISSING FILES ({len(missing_files)} pcs):\n")
        f.write("-" * 70 + "\n")
        if missing_files:
            for file in sorted(missing_files):
                f.write(f"   - {file}\n")
        else:
            f.write("   No missing files\n")
        
        f.write("\n" + "-" * 70 + "\n")
        f.write(f"✅ PRESENT FILES FROM LIST ({len(common_files)} pcs):\n")
        f.write("-" * 70 + "\n")
        for file in sorted(common_files):
            f.write(f"   + {file}\n")
        
        if extra_files:
            f.write("\n" + "-" * 70 + "\n")
            f.write(f"⚠️ EXTRA FILES (not in list) ({len(extra_files)} pcs):\n")
            f.write("-" * 70 + "\n")
            for file in sorted(extra_files):
                f.write(f"   ! {file}\n")
    
    print(f"\n💾 Detailed report saved to: {result_file}")
    
    return missing_files, extra_files, common_files

# ============= MAIN PROGRAM =============

if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 70)
    print("FILE COMPARISON TOOL (ignores numbering)")
    print("=" * 70)
    print(f"Working folder: {folder}\n")
    
    # Automatically find list files
    possible_lists = [f for f in os.listdir(folder) if f.endswith('.txt') and f != "comparison_result.txt"]
    
    if possible_lists:
        print("Found txt files that could be lists:")
        for i, f in enumerate(possible_lists, 1):
            print(f"   {i}. {f}")
        print(f"   {len(possible_lists)+1}. Specify another file")
        
        choice = input(f"\nSelect file (1-{len(possible_lists)+1}): ").strip()
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(possible_lists):
                reference_file = possible_lists[choice_num - 1]
            else:
                reference_file = input("Enter the list file name: ").strip()
        except:
            reference_file = input("Enter the list file name: ").strip()
    else:
        reference_file = input("Enter the list file name (e.g., file_list.txt): ").strip()
    
    if not reference_file:
        reference_file = "file_list.txt"
    
    # Run comparison
    missing, extra, common = compare_with_reference_list(folder, reference_file)