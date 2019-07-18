function [A] = meanNormalization(v)
  A = (v-mean(v))/range(v);
endfunction