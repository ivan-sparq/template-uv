#!/bin/bash
# Test script for version bumping logic

echo "Testing version bumping logic..."

# Test cases
test_cases=(
    "0.1.0:0.2.0"
    "1.5.3:1.6.0"
    "2.0.1:2.1.0"
    "0.1.alpha1:0.2.alpha0"
    "1.0.beta5:1.1.beta0"
)

for test_case in "${test_cases[@]}"; do
    input_version=$(echo "$test_case" | cut -d: -f1)
    expected_output=$(echo "$test_case" | cut -d: -f2)

    echo "Testing: $input_version -> $expected_output"

    # Simulate the version bumping logic
    if [[ $input_version =~ ^([0-9]+)\.([0-9]+)\.(([a-z]+)?([0-9]+))$ ]]; then
        MAJOR="${BASH_REMATCH[1]}"
        MINOR="${BASH_REMATCH[2]}"
        RELEASE="${BASH_REMATCH[4]}"
        BUILD="${BASH_REMATCH[5]}"

        # Increment minor version, reset build to 0
        NEW_MINOR=$((MINOR + 1))
        NEW_VERSION="${MAJOR}.${NEW_MINOR}.${RELEASE}0"

        if [ "$NEW_VERSION" = "$expected_output" ]; then
            echo "  ✅ PASS: $input_version -> $NEW_VERSION"
        else
            echo "  ❌ FAIL: Expected $expected_output, got $NEW_VERSION"
        fi
    else
        echo "  ❌ FAIL: Invalid version format: $input_version"
    fi
done

echo "Test completed!"
