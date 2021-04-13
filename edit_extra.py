'''INFO
Name:        edit_extra
Description: Use extra editors that you need to install prior to using them 
Author(s):   Robert Furr
Year:        2021
This and all other command sets are licensed under the GNU General Public License, see the LICENSE file included with DSAK for details.'''

from dsaklib.cmdpkg.core.editors import *

def nvim(args=None,sudo=False):
    '''Runs neovim (incomplete)'''
    edit('nvim')
