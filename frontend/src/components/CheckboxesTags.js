import React, { useEffect } from 'react';
import Checkbox from '@mui/material/Checkbox';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import CheckBoxIcon from '@mui/icons-material/CheckBox';

const icon = <CheckBoxOutlineBlankIcon fontSize="small" />;
const checkedIcon = <CheckBoxIcon fontSize="small" />;

export default function CheckboxesTags(props) {
  const myInterestings = props.myValue;
  const setMyInterestings = props.myFunc;
  const checkHandler = (isChecked, interest) => {
    if (isChecked) {
      myInterestings.add(interest.value);
      setMyInterestings(myInterestings);
      // console.log(myInteresting);
    } else if (!isChecked && myInterestings.has(interest.value)) {
      myInterestings.delete(interest.value);
      setMyInterestings(myInterestings);
      // console.log(myInteresting);
    }
  };

  return (
    <Autocomplete
      multiple
      id="interestings"
      name="interestings"
      options={interestings}
      disableCloseOnSelect
      getOptionLabel={(option) => option.name}
      renderOption={(props, option, { selected }) => (
        <li {...props}>
          <Checkbox
            icon={icon}
            checkedIcon={checkedIcon}
            style={{ marginRight: 8 }}
            checked={selected}
            onChange={checkHandler(selected, option)}
          />
          {option.name}
        </li>
      )}
      style={{ width: 500 }}
      renderInput={(params) => (
        <TextField {...params} label="관심 분야" placeholder="다중 선택 가능" color={props.color} value={[...myInterestings]} name="interestings" />
      )}
    />
  );
}

const interestings = [
  {name: "프론트엔드", value: "frontend"}, 
  {name: "백엔드", value: "backend"}, 
  {name: "데브옵스", value: "devops"}, 
  {name: "데이터 엔지니어", value: "dataengineer"}, 
  {name: "데이터 사이언티스트", value: "datascientist"}, 
  {name: "모바일", value: "mobile"}, 
  {name: "임베디드", value: "embedded"},
];