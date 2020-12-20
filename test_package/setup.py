from setuptools import setup

package_name = 'test_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xilinx',
    maintainer_email='balintmaci@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_pub = test_package.simple_pub:main',
            'simple_sub = test_package.simple_sub:main',
            'hello_node = test_package.hello_node:main'
        ],
    },
)