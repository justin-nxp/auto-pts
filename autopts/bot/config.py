#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2018, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

# Sample user_config file
# Apply your changes and rename it to config.py

from autopts.bot.iut_config.zephyr import iut_config

BotProjects = []

z = zephyr_nrf52 = {
    'name': 'zephyr'
}

# ****************************************************************************
# AutoPTS configuration
# ****************************************************************************
z['auto_pts'] = {
    #'server_ip': ['10.193.101.88'],
    #'local_ip': ['10.193.101.185'],
    # 'cli_port': [65001, 65003],
    # 'srv_port': [65000, 65002],
    'tty_file': 'COM1',
    'project_path': 'autopts/ptsprojects/boards/nxp_rt1060',
    'workspace': 'zephyr-master',
    'database_file': 'nxprtxTestCase.db',
    'store': True,
    'board': 'nxp_rt1060',
    'enable_max_logs': False,
    # 'retry': 2,
    # 'bd_addr': '',
    # 'ykush': '3',  # 1|2|3|a
    # 'recovery': False,
    'superguard': 5,  # minutes
}

# ****************************************************************************
# IUT configuration
#
# To apply test case specific changes in IUT configuration
# ****************************************************************************

z['iut_config'] = iut_config


BotProjects.append(zephyr_nrf52)
