import { describe, expect, test } from 'vitest';
import Subtraction from '../subtraction';

describe('Correct Subtraction values', () => {
    test('Correct type value', () => {
        expect(new Subtraction(2, 1).type).to.eq(1);
    });

    test('Correct answer value', () => {
        for (let i = 0; i < 20; i++) {
            const question = new Subtraction(Math.floor(Math.random() * 9 + 2), Math.random());
            let answer = question.variables[0];
            for (let j = 1; j < question.variables.length; j++) {
                answer -= question.variables[j];
            }
            expect(question.answer[0]).to.eq(answer);
        }
    });
});

describe('Error throwing', () => {
    test('Level -1 - Should error', () => {
        expect(() => new Subtraction(-1, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Subtraction" has a minimum level of "2", whereas the current level is "-1"]`,
        );
    });
    test('Level 0 - Should error', () => {
        expect(() => new Subtraction(0, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Subtraction" has a minimum level of "2", whereas the current level is "0"]`,
        );
    });
    test('Level 1 - Should error', () => {
        expect(() => new Subtraction(1, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Subtraction" has a minimum level of "2", whereas the current level is "1"]`,
        );
    });

    test('Level 2 - Should not error', () => {
        expect(() => new Subtraction(2, 77)).not.toThrowError();
    });
    test('Level 3 - Should not error', () => {
        expect(() => new Subtraction(3, 77)).not.toThrowError();
    });

    test('Level 10 - Should not error', () => {
        expect(() => new Subtraction(10, 77)).not.toThrowError();
    });
    test('Level 11 - Should not error', () => {
        expect(() => new Subtraction(11, 77)).not.toThrowError();
    });
    test('Level 12 - Should not error', () => {
        expect(() => new Subtraction(12, 77)).not.toThrowError();
    });

    test('Level 13 - Should error', () => {
        expect(() => new Subtraction(13, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Subtraction" has a maximum level of "2", whereas the current level is "13"]`,
        );
    });
    test('Level 14 - Should error', () => {
        expect(() => new Subtraction(14, 77)).toThrowErrorMatchingInlineSnapshot(
            `[Error: Question of type "Subtraction" has a maximum level of "2", whereas the current level is "14"]`,
        );
    });
});
