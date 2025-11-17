#!/bin/bash
# Deployment script for AgentText Python package

set -e

echo "🚀 AgentText Python Package Deployment"
echo "======================================"
echo ""

# Check if dist files exist
if [ ! -d "dist" ] || [ -z "$(ls -A dist)" ]; then
    echo "❌ No distribution files found. Building package..."
    python -m build
fi

echo "✅ Distribution files ready:"
ls -lh dist/
echo ""

# Ask which repository to upload to
echo "Select upload target:"
echo "1) TestPyPI (recommended for first upload)"
echo "2) PyPI (production)"
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "📦 Uploading to TestPyPI..."
    echo "You'll need TestPyPI credentials:"
    echo "  - Username: Your TestPyPI username"
    echo "  - Password: Your TestPyPI password or API token"
    echo ""
    twine upload --repository testpypi dist/*
    echo ""
    echo "✅ Uploaded to TestPyPI!"
    echo "Test installation with:"
    echo "  pip install --index-url https://test.pypi.org/simple/ agenttext"
elif [ "$choice" = "2" ]; then
    echo ""
    echo "📦 Uploading to PyPI (production)..."
    echo "⚠️  WARNING: This will publish to production PyPI!"
    echo "You'll need PyPI credentials:"
    echo "  - Username: Your PyPI username (or __token__ for API token)"
    echo "  - Password: Your PyPI password or API token"
    echo ""
    read -p "Continue? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
        twine upload dist/*
        echo ""
        echo "✅ Uploaded to PyPI!"
        echo "Install with: pip install agenttext"
    else
        echo "❌ Upload cancelled"
    fi
else
    echo "❌ Invalid choice"
    exit 1
fi

