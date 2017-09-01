# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\..\\cardgameend\\cardGame\\main_game_loop.py'],
             pathex=['C:\\Users\\berlin\\Desktop\\\xd1\xa7\xcf\xb0\\\xca\xb5\xd1\xb5\xbf\xa8\xc5\xc6\\CARDGA~2\\cardGame'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          exclude_binaries=True,
          name='main_game_loop',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main_game_loop')
