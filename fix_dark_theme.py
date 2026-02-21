"""
Script to fix dark theme text visibility in all templates
"""
import os
import re

def fix_template(filepath):
    """Fix dark theme colors in a template file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Skip if already using base_dark.html or if it's a base template
        if 'base_dark.html' in content or os.path.basename(filepath).startswith('base'):
            return False
        
        # Replace light theme colors with dark theme equivalents
        replacements = [
            # Background colors
            (r'bg-white\b', 'bg-gray-800'),
            (r'bg-gray-50\b', 'bg-gray-750'),
            (r'bg-gray-100\b', 'bg-gray-700'),
            (r'bg-gray-200\b', 'bg-gray-700'),
            
            # Text colors
            (r'text-gray-900\b', 'text-gray-100'),
            (r'text-gray-800\b', 'text-gray-100'),
            (r'text-gray-700\b', 'text-gray-200'),
            (r'text-gray-600\b', 'text-gray-300'),
            (r'text-gray-500\b', 'text-gray-400'),
            (r'(?<!")text-black\b', 'text-gray-100'),
            
            # Border colors
            (r'border(?!-)\b', 'border border-gray-700'),
            (r'border-gray-200\b', 'border-gray-700'),
            (r'border-gray-300\b', 'border-gray-600'),
            
            # Hover states
            (r'hover:bg-gray-50\b', 'hover:bg-gray-750'),
            (r'hover:bg-gray-100\b', 'hover:bg-gray-700'),
            (r'hover:bg-gray-200\b', 'hover:bg-gray-700'),
            (r'hover:bg-gray-300\b', 'hover:bg-gray-600'),
            
            # Badge/Tag colors (keep contrast but adjust)
            (r'bg-blue-100\b', 'bg-blue-900'),
            (r'text-blue-800\b', 'text-blue-300'),
            (r'bg-purple-100\b', 'bg-purple-900'),
            (r'text-purple-800\b', 'text-purple-300'),
            (r'bg-green-100\b', 'bg-green-900'),
            (r'text-green-800\b', 'text-green-300'),
            (r'bg-red-100\b', 'bg-red-900'),
            (r'text-red-800\b', 'text-red-300'),
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # If content changed, write it back
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all templates"""
    templates_dir = r'c:\Users\laksh\OneDrive\Desktop\skill_swap\templates'
    count = 0
    
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if fix_template(filepath):
                    count += 1
                    print(f"Fixed: {filepath}")
    
    print(f"\nTotal files updated: {count}")

if __name__ == '__main__':
    main()
