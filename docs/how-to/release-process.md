# How to make a release

1. create a new release branch `git checkout -b release/X.Y.Z`
1. bump the package version `tbump X.Y.Z`
1. commit the changes `git commit -m "bump version to X.Y.Z"`
1. push the changes `git push origin release/X.Y.Z`
1. create a pull request to merge the changes into the main branch `gh pr create --base main`
1. merge the pull request `gh pr merge `
1. create a new release on GitHub `gh release create X.Y.Z`
