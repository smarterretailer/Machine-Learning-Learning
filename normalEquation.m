function [A] = normalEquation(X, y)
  A = pinv(X'*X)*X'*y;
endfunction
  