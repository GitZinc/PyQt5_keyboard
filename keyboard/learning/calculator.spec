# -*- mode: python -*-

block_cipher = None


a = Analysis(['calculator.py'],
             pathex=['D:\\python3.6\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\python3.6\\Lib\\site-packages\\PyQt5\\Qt\\plugins', 'D:\\fengru\\keyboard\\learning'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='calculator',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
