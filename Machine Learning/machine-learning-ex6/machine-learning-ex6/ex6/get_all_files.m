files = dir('spam_2\*');
for idx = 1:length(files)
   file_name = files(idx).name;
   fprintf("Processing File %s\n",file_name);
   ##data=importdata(file_name);
   data=textscan(file_name);
   [filepath,name,ext] = fileparts(fullfile(pwd,file_name));
   save(['spam_2\',name '.mat'],'data');
end

Folder = 'spam_2\';
FileList = dir(fullfile(Folder, '*.mat'));  % List of all MAT files
allData  = struct();
for iFile = 1:numel(FileList)               % Loop over found files
  Data   = load(fullfile(Folder, FileList(iFile).name));
  Fields = fieldnames(Data);
  for iField = 1:numel(Fields)              % Loop over fields of current file
    aField = Fields{iField};
    if isfield(allData, aField)             % Attach new data:
       allData.(aField) = [allData.(aField), Data.(aField)];
    else
       allData.(aField) = Data.(aField);
    end
  end
end
save(fullfile(Folder, 'AllData.mat'), '-struct', 'allData');