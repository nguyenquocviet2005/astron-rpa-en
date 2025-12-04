#!/bin/sh
mysql -uroot -p'rpa123456' -D rpa -se "SELECT atom_content FROM c_atom_meta WHERE atom_key='atomCommon'"
