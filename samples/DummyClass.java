package com.kakawait;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Sample
 *
 * @version 1
 */
public class DummyClass {

    interface Formula {
        double calculate(int a);

        default double sqrt(int a) {
            return Math.sqrt(positive(a));
        }

        static int positive(int a) {
            return a > 0 ? a : 0;
        }
    }

    public void formule() {
        Formula formula = new Formula() {
            @Override
            public double calculate(int a) {
                return sqrt(a * 100);
            }
        };

        formula.calculate(100);     // 100.0
        formula.sqrt(-23);          // 0.0
        Formula.positive(-4);       // 0.0
    }

    public void lambda() {
        try (Stream<String> stream = Files.lines(Paths.get("res/nashorn1.js"))) {
            stream.filter(line -> line.contains("print"))
                    .map(String::trim)
                    .forEach(System.out::println);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void pattern() {
        String string = Pattern.compile("[:_-]")
                .splitAsStream("foobar:foo:bar")
                .filter(s -> s.contains("bar"))
                .sorted()
                .collect(Collectors.joining(":"));
        System.out.println(string);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}