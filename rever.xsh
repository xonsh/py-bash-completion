$PROJECT = $GITHUB_REPO = 'py-bash-completion'
$GITHUB_ORG = 'xonsh'

$ACTIVITIES = ['version_bump', 'changelog',
               'tag', 'push_tag', 'pypi',
               'ghrelease']

$VERSION_BUMP_PATTERNS = [
    ('bash_completion.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'VERSION\s*=.*', "VERSION = '$VERSION'")
    ]
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_TEMPLATE = 'TEMPLATE.rst'
