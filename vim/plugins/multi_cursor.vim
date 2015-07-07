let g:neocomplete#enable_insert_char_pre = 1
let g:neocomplete#enable_at_startup = 0
autocmd VimEnter * NeoCompleteEnable    " Workaround to make multiple-cursors fast
" << cut >>
" Make multiple cursors fast with neocomplete
function! Multiple_cursors_before()
    exe 'NeoCompleteDisable'
endfunction

function! Multiple_cursors_after()
    exe 'NeoCompleteEnable'
endfunction
